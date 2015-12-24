$('#startDeluge').click(function () {
	$.post('/api/start/deluge', function (data) {
		printCmd(data.cmd);
	});
}); 

$('#stopDeluge').click(function () {
	$.post('/api/stop/deluge', function (data) {
		printCmd(data.cmd);
	});
});

$('#restartDeluge').click(function () {
	console.log("Restart deluge");
});

$('#startSamba').click(function () {
	$.post('/api/start/samba', function (data) {
		printCmd(data.cmd);
	});
});

$('#stopSamba').click(function () {
	$.post('/api/stop/samba', function (data) {
		printCmd(data.cmd);
	});
});

$('#restartSamba').click(function () {
	console.log("Restart samba");
});

$('#shutdown').click(function () {
	console.log("Shutdown the pi");
});

$('#reboot').click(function () {
	console.log("Reboot the pi");
});

function printCmd(cmd) {
	if (cmd) {
		Materialize.toast("System ran: '" + cmd + "'", 5000);
	} else {
		Materialize.toast("An error has occured");
	}
}