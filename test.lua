--- -
---- Created by IntelliJ IDEA.
---- User: zannb
---- Date: 2018/2/6
---- Time: 7:39
---- To change this template use File | Settings | File Templates.
----
--
-- local http=require("socket.http");
--
-- local request_body = [[login=user&password=123]]
-- local response_body = {}
--
---- local res, code, response_headers = http.request{
---- url = "http://httpbin.org/post",
---- method = "POST",
---- headers =
---- {
---- ["Content-Type"] = "application/x-www-form-urlencoded";
---- ["Content-Length"] = #request_body;
---- },
---- source = ltn12.source.string(request_body),
---- sink = ltn12.sink.table(response_body),
---- }
--
-- local url = 'http://alihz-debug.qbtrade.org:44444/'
--
-- local request_body = [[hello=1&fuck=2]]
-- local response_body={}
-- local res, code, response_headers = http.request {
-- url = url..'/getjson',
-- method = 'POST',
-- headers =
-- {
-- ["Content-Type"] = "application/x-www-form-urlencoded";
-- ["Content-Length"] = #request_body;
-- },
-- source = ltn12.source.string(request_body),
-- sink = ltn12.sink.table(response_body),
-- }
--
-- print(res)
-- print(code)
--
-- if type(response_headers) == "table" then
-- for k, v in pairs(response_headers) do
-- print(k, v)
-- end
-- end
--
-- print("Response body:")
-- if type(response_body) == "table" then
-- for k,v in pairs(response_body) do
-- print(k .. ':' .. v)
-- end
-- else
-- print("Not a table:", type(response_body))
-- end


--t={
--    ['hellp'] = 'bobo',
--    ['yes'] = 'ok'
--}
--
--local json = require "json"
--print(json.encode(t))
--- -print(type(json.encode(response_body[1])))
-- local http = require "socket.http"
--
-- function printToLogServer(raw)
-- local postbody= {}
-- if type(raw) == "string" then
-- print('get string')
-- postbody = {
-- ["msg"] = raw
-- }
-- elseif type(raw) == "table" then
-- print('get table')
-- postbody = raw
-- end
-- postbody = json.encode(postbody)
-- print(postbody)
-- http.request{
---- url= "http://alihz-debug.qbtrde.org:44444/getjson",
-- url = "http://localhost:44444/tolog",
-- method="POST",
-- headers =
-- {
-- ["Content-Type"] = "application/x-www-form-urlencoded";
-- ["Content-Length"] = #postbody;
-- },
-- source = ltn12.source.string(postbody),
-- }
-- end
--
--
-- local h = {
-- ['waht'] = 12,
-- ['wofl'] = 'strafsaf',
-- }
---- h= json.encode(h)
-- printToLogServer(h)

local jwt = {
    ['hello'] = 'yes',
    ['fuck'] = {
        ['nope'] = 'ok',
        ['t'] = 'dddd',
    }
}

for k, v in pairs(jwt) do
    print('k:' .. k)
    if type(v) == 'string' then
        print('v:' .. v)
    elseif type(v) == 'table' then
        for kk, vv in pairs(v) do
            print('v:' .. kk .. ':' .. vv)
        end
    end
end

local function is_in_table(v, t)
    for kk, vv in pairs(t) do
        print(vv)
        print(v)
        if vv == v then
            return true
        end
    end
    return false
end

print(is_in_table('yes', jwt))

if 1 == nil then
    print('h')
else
    print('ff')
end