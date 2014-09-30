app.controller('bookController', ['$http', '$scope', 'ngDialog','$state', function ($http, $scope, ngDialog,$state){

    $http.get('http://127.0.0.1:8000/books/book/?format=json').success (function(data){
		$scope.books = data.objects;
	});

    $scope.deleteBook = function(id){
        $http({
                url: 'http://127.0.0.1:8000/deletebook/',
                method: 'POST',
                data: {"id": id}
        }).then(function(result) {
            $state.go($state.current, {}, {reload: true});
        });
    };

    $scope.addBook = function () {
        ngDialog.open({ 
            template: 'templates/popup-addBook.html', 
            controller:'addBookController', 
            scope: $scope 
        });
    };

    $scope.editBook = function(id, title, publisher, year){
        ngDialog.open({ 
            template: 'templates/popup-editBook.html', 
            controller:'editBookController',
            data: { "id": id, "title": title, "publisher": publisher, "year": year },
            scope: $scope
        });
    };

}]);

app.controller('publisherController', ['$http', '$scope', function ($http, $scope){
    $http.get('http://127.0.0.1:8000/publishers/publisher/?format=json').success (function(data){
        $scope.publishers = data.objects;
    });
}]);

app.controller('addBookController', ['$http', '$scope', '$filter','$state','allYears', function ($http, $scope, $filter,$state,allYears){
    $scope.years = allYears.years();

    $http.get('http://127.0.0.1:8000/publishers/publisher/?format=json').success (function(data){
        $scope.publishers = data.objects;
    });

    $scope.newbook = function(){
        if ($scope.myForm.$valid) {
            $http({
                url: 'http://127.0.0.1:8000/addbook/',
                method: 'POST',
                data: {"title": $scope.myTitle, "publisher": $scope.myPub, "year": $scope.myYear}
            }).then(function(result) {
                $state.go($state.current, {}, {reload: true});
            });
        } else {
            $scope.myForm.submitted = true;
        }
    };
}]);

app.controller('editBookController', ['$http', '$scope', '$filter','$state','allYears', function ($http, $scope, $filter,$state,allYears){
    $scope.years = allYears.years();
    $scope.myYear = $scope.ngDialogData.year;

    $http.get('http://127.0.0.1:8000/publishers/publisher/?format=json').success (function(data){
        $scope.publishers = data.objects;
        $scope.myPub = $filter('filter')($scope.publishers, {"fullname": $scope.ngDialogData.publisher})[0].id;
    });

    $scope.updatebook = function(){
        if ($scope.myForm.$valid) {
            $http({
                url: 'http://127.0.0.1:8000/editbook/',
                method: 'POST',
                data: {"id": $scope.ngDialogData.id, "title": $scope.myTitle, "publisher": $scope.myPub, "year": $scope.myYear}
            }).then(function(result) {
                $state.go($state.current, {}, {reload: true});
            });
        } else {
            $scope.myForm.submitted = true;
        }
    };
}]);