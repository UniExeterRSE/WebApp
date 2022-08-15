class Client {
    // == Navigation ==
    static go_to_splashpage() {
        window.location.replace("/");
    }

    // == Sample ==
    static mandelbrot(real, imag, success, error) {
        $.ajax({
            url: "/mandelbrot",
            type: "GET",
            dataType: "html",
            contentType: "application/json",
            data: JSON.stringify({
                real: real,
                imag: imag,
            }),
            success: success,
            error: error,
        });
    }
}
