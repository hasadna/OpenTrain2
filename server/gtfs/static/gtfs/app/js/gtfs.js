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


app.controller('SelectStopsController', ['$scope', 'MyHttp',
    function ($scope, MyHttp) {
        $scope.input = {
            dt: new Date()
        };

        $scope.formats = ['dd-MMMM-yyyy', 'yyyy/MM/dd', 'dd.MM.yyyy', 'shortDate'];
        $scope.format = $scope.formats[0];

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
            })
    }
]);

