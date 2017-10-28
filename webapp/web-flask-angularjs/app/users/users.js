'use strict';

angular.module('myApp.users', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/users', {
    templateUrl: 'users/users.html',
    controller: 'UsersCtrl'
  });
}])

.controller('UsersCtrl', ['$scope', '$http', '$window', 'UserService', function($scope, $http, $window, UserService) {
    $scope.users = [];
    
    function list() {
        $http({
            method: 'GET',
            url: 'http://localhost:5000/users'
        }).then(function(response) {
            var users = response.data.users;
            for (var i = 0; i < users.length; i++) {
                $scope.users.push(users[i]);
            }
        }, function(error) {
            console.log(error);
        });
    }
    
    $scope.showMessage = function() {
        if ($scope.users.length === 0) {
            return true;
        }
        return false;
    }
    
    list();
    
}]);