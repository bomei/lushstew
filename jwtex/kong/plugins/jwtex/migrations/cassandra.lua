local plugin_config_iterator = require("kong.dao.migrations.helpers").plugin_config_iterator

return {
    {
        name = "2015-06-09-jwtex-auth",
        up = [[
      CREATE TABLE IF NOT EXISTS jwtex_secrets(
        id uuid,
        consumer_id uuid,
        key text,
        secret text,
        created_at timestamp,
        PRIMARY KEY (id)
      );

      CREATE INDEX IF NOT EXISTS ON jwtex_secrets(key);
      CREATE INDEX IF NOT EXISTS ON jwtex_secrets(secret);
      CREATE INDEX IF NOT EXISTS ON jwtex_secrets(consumer_id);
    ]],
        down = [[
      DROP TABLE jwtex_secrets;
    ]]
    },
    {
        name = "2016-03-07-jwtex-alg",
        up = [[
      ALTER TABLE jwtex_secrets ADD algorithm text;
      ALTER TABLE jwtex_secrets ADD rsa_public_key text;
    ]],
        down = [[
      ALTER TABLE jwtex_secrets DROP algorithm;
      ALTER TABLE jwtex_secrets DROP rsa_public_key;
    ]]
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
