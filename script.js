// script.js - Client-side script to handle interactions with the web interface

document.addEventListener('DOMContentLoaded', function() {
    const generateButton = document.getElementById('generate-btn');
    const contentOutput = document.getElementById('content-output');
    const userInput = document.getElementById('user-input');
    const contentTypeSelect = document.getElementById('content-type-select');
    const errorDisplay = document.getElementById('error-display');

    // Function to post data to the server and handle the response
    async function generateContent() {
        const inputText = userInput.value;
        const contentType = contentTypeSelect.value;

        // Clear previous results and errors
        contentOutput.textContent = '';
        errorDisplay.textContent = '';

        // Check if the input is not empty
        if (!inputText.trim()) {
            errorDisplay.textContent = 'Please enter some text to generate content.';
            return;
        }

        try {
            // Send the request to the server
            const response = await fetch('/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: inputText, type: contentType })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();

            // Display the generated content
            if (data && data.generatedText) {
                contentOutput.textContent = data.generatedText;
            } else {
                errorDisplay.textContent = 'Failed to generate content. Please try again.';
            }
        } catch (error) {
            console.error('Error generating content:', error);
            errorDisplay.textContent = 'An error occurred while generating content.';
        }
    }

    // Event listener for the generate button
    generateButton.addEventListener('click', generateContent);

    // Optional: Implement additional client-side logic, such as content type selection,
    // input validation, character count, etc., based on project requirements.
});
