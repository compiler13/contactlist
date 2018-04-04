var app = angular.module('myApp', []);

app.controller('myCtrl', function($scope, $http) {


    // $http.get("http://127.0.0.1:8000/contact-list/")
    // .then(function(response) {
    //     $scope.data = response.data; 
    // });
 $http({

method : "POST",
url : "",

data : {name: 'shawon' }


 }).then(function(response)

{
    $scope.name = response.data;
}

)
    
});