$(document).ready(function() {
	$('#like_btn').click(function() {
		var cateteamIdVar;
		cateteamIdVar = $(this).attr('data-teamid');
		
		$.get('/builder/like_team/',
			{'category_id': cateteamIdVar},
			function(data) {
				$('#like_count').html(data);
				$('#like_btn').hide();
			})
	});
});