local plugin_config_iterator = require("kong.dao.migrations.helpers").plugin_config_iterator

return {
    {
        name = "2015-06-09-jwtex-auth",
        up = [[
      CREATE TABLE IF NOT EXISTS jwtex_secrets(
        id uuid,
        consumer_id uuid REFERENCES consumers (id) ON DELETE CASCADE,
        key text UNIQUE,
        secret text UNIQUE,
        created_at timestamp without time zone default (CURRENT_TIMESTAMP(0) at time zone 'utc'),
        PRIMARY KEY (id)
      );

      DO $$
      BEGIN
        IF (SELECT to_regclass('jwtex_secrets_key')) IS NULL THEN
          CREATE INDEX jwtex_secrets_key ON jwtex_secrets(key);
        END IF;
        IF (SELECT to_regclass('jwtex_secrets_secret')) IS NULL THEN
          CREATE INDEX jwtex_secrets_secret ON jwtex_secrets(secret);
        END IF;
        IF (SELECT to_regclass('jwtex_secrets_consumer_id')) IS NULL THEN
          CREATE INDEX jwtex_secrets_consumer_id ON jwtex_secrets(consumer_id);
        END IF;
      END$$;
    ]],
        down = [[
      DROP TABLE jwtex_secrets;
    ]]
    },
    {
        name = "2016-03-07-jwtex-alg",
        up = [[
      ALTER TABLE jwtex_secrets ADD COLUMN algorithm text;
      ALTER TABLE jwtex_secrets ADD COLUMN rsa_public_key text;
    ]],
        down = [[
      ALTER TABLE jwtex_secrets DROP COLUMN algorithm;
      ALTER TABLE jwtex_secrets DROP COLUMN rsa_public_key;
    ]]
    },
    {
        name = "2017-05-22-jwtex_secret_not_unique",
        up = [[
      ALTER TABLE jwtex_secrets DROP CONSTRAINT IF EXISTS jwtex_secrets_secret_key;
    ]],
        down = [[
      ALTER TABLE jwtex_secrets ADD CONSTRAINT jwtex_secrets_secret_key UNIQUE(secret);
    ]],
    },
    {
        name = "2017-07-31-120200_jwtex-auth_preflight_default",
        up = function(_, _, dao)
            for ok, config, update in plugin_config_iterator(dao, "jwtex") do
                if not ok then
                    return config
                end
                if config.run_on_preflight == nil then
                    config.run_on_preflight = true
                    local _, err = update(config)
                    if err then
                        return err
                    end
                end
            end
        end,
        down = function(_, _, dao) end -- not implemented
    },
    {
        name = "2017-10-25-211200_jwtex_cookie_names_default",
        up = function(_, _, dao)
            for ok, config, update in plugin_config_iterator(dao, "jwtex") do
                if not ok then
                    return config
                end
                if config.cookie_names == nil then
                    config.cookie_names = {}
                    local _, err = update(config)
                    if err then
                        return err
                    end
                end
            end
        end,
        down = function(_, _, dao) end -- not implemented
    },
}
