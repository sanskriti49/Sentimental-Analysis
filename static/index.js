document.querySelector("form").addEventListener("submit", function () {
	console.log("Form submitted, clearing textarea...");
	document.querySelector("#review").value = ""; // Clear the textarea
	const predictedSentiment = document.querySelector(".predicted_sentiment");
	if (predictedSentiment) {
		console.log("Hiding predicted sentiment...");
		predictedSentiment.style.display = "none"; // Hide sentiment text
	}
});

window.addEventListener("load", function () {
	const predictedSentiment = document.querySelector(".predicted_sentiment");
	const originalReview = document.querySelector("#review");

	// Clear the review and hide sentiment
	if (originalReview) originalReview.value = "";
	if (predictedSentiment) predictedSentiment.style.display = "none";
});
