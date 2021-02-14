$(document).ready(function(){
	var ShowForm = function(){
		var btn = $(this);
		$.ajax({
			url: btn.attr("data-url"),
			type: 'get',
			dataType:'json',
			beforeSend: function(){
				$('#crud-modal').modal('show');
			},
			success: function(data){
				$('#crud-modal .modal-content').html(data.html_form);
			}
		});
	};

	var SaveForm =  function(){
		var form = $(this);
		$.ajax({
			url: form.attr('data-url'),
			data: form.serialize(),
			type: form.attr('method'),
			dataType: 'json',
			success: function(data){
				if(data.form_is_valid){
					$('#daftar-table tbody').html(data.daftar_list);
					$('#crud-modal').modal('hide');
				} else {
					$('#crud-modal .modal-content').html(data.html_form)
				}
			}
		})
		return false;
	}

// create 
$(".show-form").click(ShowForm);
$("#crud-modal").on("submit",".create-daftar-form",SaveForm);

//update
//$('#book-table').on("click",".show-form-update",ShowForm);
//$('#crud-modal').on("submit",".update-form",SaveForm)

//delete
//$('#book-table').on("click",".show-form-delete",ShowForm);
//$('#crud-modal').on("submit",".delete-form",SaveForm)
});