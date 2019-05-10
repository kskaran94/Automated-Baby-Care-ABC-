$(document).ready( function() {
		function readURL(input) {
		    if (input.files && input.files[0]) {
		        var reader = new FileReader();
		        file1 = input.files[0]

		        reader.onload = function (e) {
		            $('#vid-upload').attr('src', e.target.result);
		            img_file = e.target.result.split(",")[1]
		            file_name = input.files[0].name;
		            $('#vid-name').text(file_name);
		        } 
		        reader.readAsDataURL(input.files[0]);
		    }
		}

		$("#VidInp").change(function(){
		    readURL(this);
		});

		$("#upload").click(function () {
			file_name = $("#vid-name").text()
			alert(file_name)
        $.ajax({
            type: 'GET',
            url: "/processVideo?filename="+file_name,
            success: function (data) {
                alert(data)
            }
        });
    });

	});



