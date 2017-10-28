'use strict';

angular.module('myApp.signin', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/signin', {
    templateUrl: 'signin/signin.html',
    controller: 'SignInCtrl'
  });
}])

.controller('SignInCtrl', ['$scope', '$http', '$window', 'UserService', function($scope, $http, $window, UserService) {
    $scope.user = {};
    $scope.errorMessage = "";
    
    $scope.login = function() {
        $scope.errorMessage = "";

        if ($scope.user.username === undefined || $scope.user.pass === undefined) {
            $scope.errorMessage = "Email & Password must be entered!";
        } else {
            $http({
                method: 'POST',
                contentType: "application/json",
                url: 'http://localhost:5000/login',
                data: {user: $scope.user}
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