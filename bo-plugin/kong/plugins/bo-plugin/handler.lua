--
-- Created by IntelliJ IDEA.
-- User: zannb
-- Date: 2018/2/11
-- Time: 13:41
-- To change this template use File | Settings | File Templates.
--

-- handler.lua
local BasePlugin = require "kong.plugins.base_plugin"
local BoPlugin = BasePlugin:extend()

local responses = require "kong.tools.responses"

function BoPlugin:new()
    BoPlugin.super.new(self, "bo-plugin")
    ngx.log(ngx.DEBUG, 'in new')
end

function BoPlugin:access(config)
    BoPlugin.super.access(self)

    ngx.log(ngx.DEBUG, 'in access')
end

return BoPlugin