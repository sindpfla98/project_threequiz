// $(function(){
// 	$(document).mouseup(function(e) {
// 		if ($(e.target).parents('.zeta-menu').length == 0) {
// 			$('.zeta-menu li').removeClass('expand');
// 			$('.zeta-menu ul').hide();
// 		}
// 	});
// 	$(".zeta-menu>li:has(ul)>a").each( function() {
// 		$(this).html( $(this).html()+' &or;' );
// 	});
// 	$(".zeta-menu ul li:has(ul)")
// 		.find("a:first")
// 		.append("<p style='float:right;margin:-3px'>&#9656;</p>");
//
// 	$(".zeta-menu li>a").click(function(){
// 		var li = $(this).parent();
// 		var ul = li.parent();
// 		ul.find('li').removeClass('expand');
// 		ul.find('ul').not(li.find('ul')).hide();
// 		li.children('ul').toggle();
// 		if( li.children('ul').is(':visible') || li.has('ul')) {
// 			li.addClass('expand');
// 		}
// 	});
// });