$(document).ready(function() {
	var items = [];
	$('.title').each(function(){
		items.push($(this).text().trim());
	})

	var interval = null;

	if (!localStorage.items) {
		localStorage.items = '';
	}
	var cache = localStorage.items.split('###');
	
	if (cache[0] != items[0]) {
		document.getElementById('sound').play();
		interval = setInterval(togglePageTitle, 500);
		localStorage.items = items.join('###');
	}

	$('.item').mouseenter(function() {
		clearInterval(interval);
	})
});


function togglePageTitle() {
	if ($(document).prop('title') == 'New items!!!') {
		$(document).prop('title', 'Blocket Spy');
	} else {
		$(document).prop('title', 'New items!!!');
	}
}