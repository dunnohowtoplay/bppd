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
        console.log(data.html_form)
				if(data.form_is_valid){
          $('#daftar-table tbody').html(data.daftar_list);
          location.reload();
          //$('#crud-modal').modal('hide');
                    
				} else {
					$('#crud-modal .modal-content').html(data.html_form)
				}
			}
		})
		return false;
    };

    var EditForm =  function(){
      var form = $(this);
      var no_pelayanans = [];
      var no_pelayanan
      $(':checkbox:checked').each(function(i){
        no_pelayanans[i]=$(this).val()
      })
      if(no_pelayanans.length===0){
        alert("Please select item to Edit")
      }else if(no_pelayanans.length>1){
        alert("Please select one item to Edit")
      }else{
        no_pelayanan = no_pelayanans[0]
        
        console.log(no_pelayanans) 
        console.log(no_pelayanan)
        $('#crud-modal').modal('show');
        $.ajax({
          url:  form.attr("data-url").replace('x',no_pelayanan),
          type: form.attr('method'),
          data: form.serialize(),
          dataType: 'json',
          success: function(data){
            if(data.form_is_valid){
              console.log(data.form_is_valid)
              $('#daftar-table tbody').html(data.daftar_list);
              location.reload();
              
              //$('#crud-modal').modal('hide');
                        
            } else {
              $('#crud-modal .modal-content').html(data.html_form)
            }
          }
        })
        return false; 
      }
    }

    var deleteDaftar =  function(){
      if(confirm("Are you sure you want to delete this data?")){
          var btn = $(this);
          var deleteid = [];
          var csrf=$('input[name=csrfmiddlewaretoken]').val();
          $(':checkbox:checked').each(function(i){
            deleteid[i]=$(this).val()
          })
          if(deleteid.length===0){
            alert("Please select item to delete")
          }else{
            console.log(deleteid)
            $.ajax({
              url:btn.attr("data-url"),
              method:"POST",
              data:{
                deleteid,
                csrfmiddlewaretoken:csrf
              },
              success:function(response){
                for(var i=0; i < deleteid.length; i++){
                  $('tr#'+deleteid[i]+'').fadeOut('slow');
                }
                location.reload();
              }
            })
          }
        }
    }

//CRUD Pendaftaran
// create 
$(".show-form").click(ShowForm);
$("#crud-modal").on("submit",".create-daftar-form",SaveForm);
//update
$('.show-form-update').on("click", EditForm);
$('#crud-modal').on("submit",".update-daftar-form", EditForm)
//delete
$('#deletependaftaran').on("click", deleteDaftar);
});