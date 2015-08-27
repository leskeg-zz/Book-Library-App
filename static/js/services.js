app.factory("allYears", function($filter) {
	var years = [];
	var currentDate = new Date();
	for (var i = $filter('date')(currentDate, 'yyyy'); i >= 0; i--) {
		years.push(i);
	}

	return {
		years: function() {
			return years;
		}
	};
});