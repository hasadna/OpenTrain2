var module = angular.module('my.utils', []);
module.factory('MyHttp', ['$http','$q',
    function ($http, $q) {
        var doHttp = function (method, url, conf) {
            var p = $http({
                method: method,
                url: url,
                params: conf.params,
                data: conf.data
            });
            return p.then(function (resp) {
                return resp.data;
            }, function (error) {
                alert(error.config.method + ' ' + error.config.url + ' result in error ' + error.status + '\n' +
                    'Details:\n' +
                    error.data
                )
                return $q.reject();
            });
        }
        var service = {
            get: function (url, params) {
                return doHttp('GET', url, {
                    params: params
                });
            }
        }
        return service;
    }]);
