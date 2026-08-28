/**
 * Cell & The Lasers - leaderboard bridge
 */

addSimMessageHandler("cell-lasers", function (data) {
    try {
        console.log("MAKECODE SCORE:", data);

        const message = JSON.stringify(data);

        window.parent.postMessage({
            type: "messagepacket",
            channel: "cell-lasers",
            data: new TextEncoder().encode(message)
        }, "*");

    } catch (error) {
        console.error("CELL-LASERS MESSAGE ERROR:", error);
    }
});
