<script>
    let message;

    fetch("http://localhost:8000/hello").then((res) => {
        res.json().then((json) => {
            message = json.message;
        });
    });
</script>

<h1>{message || "svelte page"}</h1>
