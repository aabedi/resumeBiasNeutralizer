angular.module('tableApp', [])

	.controller('mainController', function($scope){
		$scope.sortType = 'fish'; //set the default sort type
		$scope.softReverse = false; // set the default sort order
		$scope.searchFish = ''; //the the default sort filter

		//create the list of sushi rolls

		$scope.sushi = [
			{ name: 'Amanda Loh', fish: 'Crab', tastiness: 2},
			{ name: 'Curren Mehta', fish: 'Tuna', tastiness: 2},
			{ name: 'Jordan Banafsheha', fish: 'Eel', tastiness: 2},
      { name: 'Jordan Banafsheha', fish: 'Eel', tastiness: 2},
      { name: 'Jordan Banafsheha', fish: 'Eel', tastiness: 2},
      { name: 'Jordan Banafsheha', fish: 'Eel', tastiness: 2},
			{ name: 'Joshua Meier', fish: 'Variety', tastiness: 6}

		];
	});
