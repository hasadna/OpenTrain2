var app = angular.module('Gtfs', ['ngRoute', 'ui.bootstrap', 'ui.bootstrap.buttons']);

var baseDir = '/static/gtfs/app'

app.config(['$routeProvider',
function($routeProvider) {
    var templateUrl = function(templateName) {
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


app.controller('SelectStopsController',['MyHttp','$scope',
    function($scope,MyHttp) {
        console.log('123');
        MyHttp.get('/api/gtfs/stops/')
            .success(function(stops) {
                $scope.stops = stops;
            })
    }
]);

