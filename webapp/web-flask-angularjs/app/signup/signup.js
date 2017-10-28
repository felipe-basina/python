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
    
    $scope.register = function() {
        $scope.errorMessage = "";

        if ($scope.auth.username === undefined || $scope.auth.pass === undefined) {
            $scope.errorMessage = "Email & Password must be entered!";
        } else {
            $http({
                method: 'POST',
                contentType: "application/json",
                url: 'http://localhost:5000/register',
                data: {auth: $scope.auth}
            }).then(function(response) {
                UserService.set(response.data);
                $window.location.href = '#home.html';
            }, function(error) {
                $scope.errorMessage = error.data.message;
            });
        }
    };
    
    $scope.showError = function() {
        if ($scope.errorMessage === "") {
            return false;
        }
        return true;
    }
    
}]);