var app = angular.module('myApp', []);

app.controller('myCtrl', function($scope, $http) {
    $scope.form = {};


    // $http.get("http://127.0.0.1:8000/contact-list/")
    // .then(function(response) {
    //     $scope.data = response.data; 
    // });
 
$scope.postContact = function () {
    console.log("hello form post");
    console.log($scope.form);
    $http({

        method : "POST",
        
        url : "http://127.0.0.1:8000/contact-list/",
        
        data: $scope.form
        
        
         }).then(function(response) {
            $scope.data = response.data;
        }).catch(function(error) {
            console.log("Error", error);
        })
} 
$scope.getContactList = function () {
    $http({

        method : "GET",
        
        url : "http://127.0.0.1:8000/contact-list/",
        
        // data : {name: 'shawon' }
        
        
         }).then(function(response) {
             console.log("helllo");
            $scope.data = response.data;
        }).catch(function(error) {
            console.log("Error", error);
        }) 
}
$scope.getContactList();
    
});

app.controller('postCtrl', function($scope, $http) {
    $scope.form = {};

$scope.postContact = function () {
    console.log("hello form post");
    console.log($scope.form);
    $http({
    method : "POST",
    
    url : "http://127.0.0.1:8000/contact-list/",
    
    data: $scope.form
    
    
        }).then(function(response) {
        $scope.data = response.data;
    }).catch(function(error) {
        console.log("Error", error);
    })
} 
    
});