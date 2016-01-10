'use strict';

(function(){
    var app = angular.module('navgar', []);
    app.controller('PostsCtrl', ['$http', function($http){
        var self = this;
        $http.get('/posts/most_popular').success(function(data){
            self.posts = data;
        });
    }]);
    app.controller('PopularUsersCtrl', ['$http', function($http){
        var self = this;
        $http.get('/users/most_popular').success(function(data){
            self.users = data;
        });
    }]);
})();

