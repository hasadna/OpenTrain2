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


app.controller('SelectStopsController', ['$scope', 'MyHttp', '$filter', '$window',
    function ($scope, MyHttp, $filter, $window) {
        var lastSearchJson = $window.localStorage.getItem('lastSearch');
        var lastSearch = lastSearchJson && JSON.parse(lastSearchJson);

        $scope.status = {
            opened: false
        };
        $scope.input = {
            dt: new Date(),
            time: new Date()
        }
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
                $scope.stopsByIds = {};
                $scope.stops.forEach(function (stop) {
                    $scope.stopsByIds[stop.id] = stop;
                });
                if (lastSearch) {
                    $scope.input.from_stop = $scope.stopsByIds[lastSearch.from_stop.id]
                    $scope.input.to_stop = $scope.stopsByIds[lastSearch.to_stop.id]
                } else {
                    $scope.input.from_stop = $scope.stops[0];
                    $scope.input.to_stop = $scope.stops[10];
                }
            });
        $scope.doSearch = function () {
            $scope.trips = null;
            $scope.from_stop = $scope.input.from_stop;
            $scope.to_stop = $scope.input.to_stop;
            $window.localStorage.setItem('lastSearch',JSON.stringify($scope.input));
            MyHttp.get('/api/gtfs/trips/from-to/', {
                date: $filter('date')($scope.input.dt, 'dd-MM-yyyy'),
                time: $filter('date')($scope.input.time, 'HH:mm'),
                from_stop: $scope.input.from_stop.id,
                to_stop: $scope.input.to_stop.id,
            }).then(function (trips) {
                $scope.trips = trips;
                $scope.showTrips();
            })
        }
        $scope.cleanTrip = function (trip, allStopIds) {
            var show = false;
            trip.timesByIds = {}
            trip.stop_times.forEach(function (st) {
                if (st.s == $scope.from_stop.id) {
                    show = true;
                }
                if (show) {
                    trip.timesByIds[st.s] = st;
                    if (allStopIds.indexOf(st.s) < 0) {
                        allStopIds.push(st.s);
                    }
                }
                if (st.s == $scope.to_stop.id) {
                    show = false;
                }
            })
        }
        $scope.showTrips = function (trips) {
            var allStopIds = [];
            $scope.trips.forEach(function (trip) {
                $scope.cleanTrip(trip, allStopIds);
            });
            $scope.tripsStops = [];
            allStopIds.forEach(function (sid) {
                $scope.tripsStops.push($scope.stopsByIds[sid]);
            });
            $scope.tripsStops.sort(function(s1,s2) {
                for (var i = 0 ; i < $scope.trips.length ; i++) {
                    var trip = $scope.trips[i];
                    if (trip.timesByIds[s1.id] && trip.timesByIds[s2.id]) {
                        return trip.timesByIds[s1.id].i - trip.timesByIds[s2.id].i > 0 ? 1 : -1;
                    }
                }
                return 0;
            })
            $scope.trips.sort(function(t1,t2) {
                var s1 = t1.timesByIds[$scope.from_stop.id];
                var s2 = t2.timesByIds[$scope.from_stop.id];
                if (s1.d > s2.d) {
                    return 1;
                }
                if (s1.d < s1.d) {
                    return -1;
                }
                return 0;
            });
        }
        $scope.getArrivalTime = function (trip, stop_id) {
            return (trip.timesByIds[stop_id] && trip.timesByIds[stop_id].a) || ''
        }
        $scope.getDepartureTime = function (trip, stop_id) {
            return (trip.timesByIds[stop_id] && trip.timesByIds[stop_id].d) || ''
        }
    }
]);


