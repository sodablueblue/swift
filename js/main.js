$(function(){
	$('#files').on('change', handleFileSelect);
})

function handleFileSelect(evt){
	var file = evt.target.files[0];

	if(!file.type.match(/xml/)){
		return errorHandler('Invalid file');
	}

	var reader = new FileReader();

	reader.onloadend = function(e){
		var xml = e.target.result.trim();
		parseXml(xml);
	}

	reader.readAsText(file, 'utf-8');
}

function parseXml(xml){
	var $content = $(xml).last();
	$content.children().each(function(i, item){

		//TODO:
		console.log(item);
	})
};

function errorHandler(message){
	console.log(message);
	return false;
};