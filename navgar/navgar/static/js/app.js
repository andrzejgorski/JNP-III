'use strict';

var serverUrl = 'http://0.0.0.0:6543';

(function(){
    var app = angular.module('navgar', []);
    app.controller('PostsCtrl', ['$http', function($http){
        var self = this;
        $http.get(serverUrl + '/posts/first').success(function(data){
            self.posts = data;
        });
    }]);
})();

