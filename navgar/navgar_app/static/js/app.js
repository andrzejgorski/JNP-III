'use strict';

(function(){
    var app = angular.module('navgar', []);
    app.controller('PostsCtrl', ['$http', function($http){
        var self = this;
        $http.get('/posts/first').success(function(data){
            self.posts = data;
        });
    }]);
})();

