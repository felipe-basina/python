'use strict';

// Declare app level module which depends on views, and components
angular.module('myApp', [
  'ngRoute',
  'myApp.version',
  'myApp.home',
  'myApp.signin',
  'myApp.signup',
  'myApp.users'
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
           user.name = data.user;
           user.message = data.message;
        },
        get: function() {
            return user;
        }
    }
}])
;
