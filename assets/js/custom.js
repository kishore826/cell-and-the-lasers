/**
 * Cell & The Lasers - leaderboard bridge
 */

addSimMessageHandler("cell-lasers", function (data) {
    try {
        console.log("MAKECODE MESSAGE RECEIVED:", data);

        // Send the message from the GitHub Pages game
        // to the outer game.html iframe.
        window.parent.postMessage({
            type: "cell-lasers-score",
            score: data.score
        }, "*");

    } catch (error) {
        console.error("CELL-LASERS MESSAGE ERROR:", error);
    }
});
