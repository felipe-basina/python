'use strict';

angular.module('myApp.signup', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/signup', {
    templateUrl: 'signup/signup.html',
    controller: 'SignUpCtrl'
  });
}])

.controller('SignUpCtrl', ['$scope', '$http', '$window', 'UserService', function($scope, $http, $window, UserService) {
    $scope.user = {};
    $scope.errorMessage = "";
    
    $scope.login = function() {
        $scope.errorMessage = "";

        if ($scope.auth.username === undefined || $scope.auth.pass === undefined) {
            $scope.errorMessage = "Email & Password must be entered!";
        } else {
            console.log("autenticação: " + JSON.stringify($scope.auth));
            $http({
                method: 'POST',
                contentType: "application/json",
                url: 'http://localhost:5000/register',
                data: {user: $scope.auth}
            }).then(function(response) {
                console.log(response);
                UserService.set(response.data);
                $window.location.href = '#home.html';
            }, function(error) {
                console.log(error);
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