'use strict';

angular.module('myApp.home', [])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/home', {
    templateUrl: 'home/home.html',
    controller: 'HomeCtrl',
    controllerAs: 'vm'
  });
}])

.controller('HomeCtrl', ['$scope', 'UserService', function($scope, UserService) {
    $scope.user = {};
    
    function init() {
        $scope.user = UserService.get();
    }
    
    $scope.isObjectEmpty = function(){
        return Object.keys($scope.user).length === 0;
    }
    
    init();    
}]);