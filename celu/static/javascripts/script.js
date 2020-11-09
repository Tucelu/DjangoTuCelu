$('#Formulario_login').show();
$('#Formulario_Registro').hide();

$('#Registrar').click(function (){
    $("#Formulario_login").hide();
    $('#Formulario_Registro').show();
});
$('#Loguearse').click(function (){
    $("#Formulario_login").show();
    $('#Formulario_Registro').hide();
});
