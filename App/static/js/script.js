const imageInput = document.getElementById("imageInput");
        const selectImageButton = document.getElementById("selectImageButton");
        const imagePreview = document.getElementById("imagePreview");

        // When the "Select Image" button is clicked, trigger the file input
        selectImageButton.addEventListener("click", function() {
            imageInput.click();
        });

        // When a file is selected, display the selected image
        imageInput.addEventListener("change", function() {
            const selectedFile = imageInput.files[0];
            if (selectedFile) {
                const reader = new FileReader();
                reader.onload = function(event) {
                    imagePreview.src = event.target.result;
                };
                reader.readAsDataURL(selectedFile);
            }
        });