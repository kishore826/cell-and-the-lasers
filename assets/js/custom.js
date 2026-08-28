console.log("CUSTOM.JS LOADED");

addSimMessageHandler("cell-lasers", function (data) {
    console.log("🔥 SCORE MESSAGE RECEIVED:", data);
});
