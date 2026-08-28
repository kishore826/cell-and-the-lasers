/**
 * Cell & The Lasers - Leaderboard
 *
 * Receives the score sent by the MakeCode Arcade game.
 */

addSimMessageHandler("cell-lasers", function (data) {
    console.log("CELL-LASERS MESSAGE RECEIVED:", data);

    if (!data) {
        console.warn("CELL-LASERS: Empty message received.");
        return;
    }

    if (typeof data.score === "number") {
        console.log("CELL-LASERS SCORE:", data.score);
    } else {
        console.warn("CELL-LASERS: Message does not contain a valid score.", data);
    }
});
