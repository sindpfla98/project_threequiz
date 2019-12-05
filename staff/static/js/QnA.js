// summernote 에디터 설정
$(document).ready(function() {
     $('#summernote').summernote({
         width: 1000,
         height: 500,
         minHeight: null,
         maxHeight: null,
         airMode: true  // 테두리가 사라짐

     });
    // 5.28 소이
    $(this).summernote("insertImage", url);

});




// 5.28 소이
//노트 쓰기 금지
$(document).ready(function(){
    // 안 써지게 막음
    $('.note-editable').attr('contenteditable', false)
});

// 질문
$(function(){
    $("tr[id^='flip_']").on("click", function(){
      var $parent = $(this).closest("tr");
      $parent.siblings().next("tr.panel").slideUp("fast");
      $(this).next("tr.panel").slideToggle("fast");
     });
});
//답변
$(function(){
    $("tr[id^='flip_']").on("click", function(){
      var $parent = $(this).closest("tr");
      $parent.siblings().next("tr.panel").next("tr.apanel").slideUp("fast");
      $(this).next("tr.panel").next("tr.apanel").slideToggle("fast");
     });
});

// 제목 클릭 시 해당 제목 글씨색 변경
$(function(){
    $("tr").on("click", function(){
        var $parent = $(this).closest("tr");
        $parent.siblings().css("color", "#000000");
        $(this).css("color", "#01A252");
    });
});

// 8.20 소이 - 알림창 디자인
function needLogin() {
    bootbox.confirm({
    message: "로그인이 필요합니다!",
    buttons: {
        confirm: {
            label: '확인',
            className: 'confirm_btn'
        },
        cancel: {
            label: '취소',
            className: 'confirm_btn'
        }
    },
    callback: function (result) {
        if(result){
            location.href ='/user/login/'
        }
    }
    });
}


