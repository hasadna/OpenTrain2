var app = angular.module('Gtfs', ['ngRoute', 'ui.bootstrap', 'ui.bootstrap.buttons', 'my.utils']);

var baseDir = '/static/gtfs/app'

app.config(['$routeProvider',
    function ($routeProvider) {
        var templateUrl = function (templateName) {
            return baseDir + '/tpls/' + templateName + '.html';
        };

        $routeProvider
            .when('/', {
                pageId: 'welcome',
                templateUrl: templateUrl('select_stops'),
                controller: 'SelectStopsController',
            })
            .otherwise({
                redirectTo: '/'
            });
    }]);


app.controller('SelectStopsController', ['$scope', 'MyHttp','$filter',
    function ($scope, MyHttp,$filter) {
        $scope.input = {
            dt: new Date(),
            time: new Date()
        };

        $scope.status = {
            opened: false
        };

        popupOptions = {
            'current-text': 'היום',
        }

        MyHttp.get('/api/gtfs/stops/')
            .then(function (data) {
                $scope.stops = data;
                $scope.stops.sort(function (s1, s2) {
                    if (s1.name > s2.name) {
                        return 1;
                    }
                    if (s1.name < s2.name) {
                        return -1;
                    }
                    return 0;
                })
                $scope.input.from_stop = $scope.stops[0];
                $scope.input.to_stop = $scope.stops[10];
            })
        $scope.doSearch = function() {
            MyHttp.get('/api/1/gtfs/trips/between/' ,{
                date: $filter('date')($scope.input.dt,'dd-MM-yyyy'),
                time: $filter('date')($scope.input.time,'HH:mm'),
                from_stop: $scope.input.from_stop.id,
                to_stop: $scope.input.to_stop.id,
            }).then(function(trips) {
                console.log(trips);
            })
        }
    }

]);

