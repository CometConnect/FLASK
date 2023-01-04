$(() => {
    $("#predict_button").click(() => {
        const text = $("#text").val();
        $.ajax({
            url: "/predict-emotion",
            type: "POST",
            data: text,
            success: (data) => {
                const response = data.split("::")
                $("#prediction").text(response[0]);
                $("#img").attr("src", response[1]);
            },
            error: () => {
                $("#prediction").text("Error");
            }
        });
    });
});

