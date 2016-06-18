/**
 * Created by aabedi on 2/9/2016.
 */
(function(angular) {
    'use strict';
    angular.module('recruitBot', ['angularUtils.directives.dirPagination'])
        .controller('ExampleController', ['$scope','$http',function($scope, $http) {
            console.log("Test");
            this.user = {
                firstName: '',
                lastName: '',
            };
            this.register = function() {
                var httpRequest = $http({
                    url: '/custQuery',
                    method: 'GET',
                    params: {firstname: this.user.firstName, lastname: this.user.lastName}
                }).success( function(data) {
                $scope.results = data;
                console.log($scope.results)});
            };
            $scope.sort = function(keyname){
                $scope.sortKey = keyname;   //set the sortKey to the param passed
                $scope.reverse = !$scope.reverse; //if true make it false and vice versa
            }
        }]);


})(window.angular);
