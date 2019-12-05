
function needTicket() {
    bootbox.alert({
    message: "응모권이 필요합니다!",
    className: 'alert_btn',
    buttons: {
      ok: {
        label: '확인'
      }
    },
    size: 'small'
    });
}

