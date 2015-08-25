var app = angular.module('myApp', [
	'ui.router',
	'ui.bootstrap',
	'ngDialog'
]);

app.config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider){
    
    $urlRouterProvider.when('/', '/books');
    $urlRouterProvider.when('/publishers', '/publishers');
    $urlRouterProvider.otherwise('/');

    $stateProvider

    .state('books',{
        url: '/books',
        templateUrl: 'static/templates/partial-books.html'
    })

    .state('publishers',{
        url: '/publishers',
        templateUrl: 'static/templates/partial-publishers.html'
    })

}]);