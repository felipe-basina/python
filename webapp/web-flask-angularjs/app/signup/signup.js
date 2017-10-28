'use strict';

angular.module('myApp.signup', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/signup', {
    templateUrl: 'signup/signup.html',
    controller: 'SignUpCtrl'
  });
}])

.controller('SignUpCtrl', ['$scope', '$http', '$window', 'UserService', function($scope, $http, $window, UserService) {
    $scope.auth = {};
    $scope.errorMessage = "";
    
    $scope.login = function() {
        $scope.errorMessage = "";

        if ($scope.auth.username === undefined || $scope.auth.pass === undefined) {
            $scope.errorMessage = "Email & Password must be entered!";
        } else {
            UserService.set($scope.auth);
            $window.location.href = '#home.html';               
        }
    };
    
    $scope.showError = function() {
        if ($scope.errorMessage === "") {
            return false;
        }
        return true;
    }
    
}]);