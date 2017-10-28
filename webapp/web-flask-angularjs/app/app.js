'use strict';

// Declare app level module which depends on views, and components
angular.module('myApp', [
  'ngRoute',
  'myApp.version',
  'myApp.home',
  'myApp.signin',
  'myApp.signup'
]).
config(['$locationProvider', '$routeProvider', function($locationProvider, $routeProvider) {
  //$locationProvider.hashPrefix('!');
  $routeProvider
    .otherwise({
        redirectTo: '/home'
    });
}])

.service('UserService', [function() {
    var user = {};
    
    return {
        set: function(data) {
           user.name = data.username;
        },
        get: function() {
            return user;
        }
    }
}])
;
