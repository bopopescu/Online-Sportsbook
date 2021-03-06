def print_style():
    return ''' <style>
    h1 {
    	text-align: center
    }

    button{
    	background-color: #ebebeb;
    	color: black;
    	padding: 14px 20px;
    	margin: 8px 0;
    	border: none;
    	cursor: pointer;
    	width: 100%;
    }

    .modal {
    	display: none;
    	position: fixed;
    	z-index: 1;
    	left: 0;
    	top: 0;
    	color: #C0C0C0;
    	width: 100%;
    	height: 100%;
    	overflow: auto;
    	background-color: rgb(0,0,0);
    	background-color: rgba(0,0,0,0.4);
    	padding-top: 60px;
    }
    .imgcontainer{
    	text-align: center;
    	margin: 24px 0 12px 0;
    	position: relative;
    }

    img.avatar{
    	width: 40%
    	border-radius: 50%;
    }

    .container{
    	padding: 16px;
    }

    span.psw{
    	float: right;
    	padding-top: 16px;
    }

    .modal-content{
    	background: -webkit-linear-gradient(top,  #0f182b 0%,#db2028 33%,#db2028 66%,#db2028 100%);
    	margin: 5px auto;
    	border: 1px solid #888;
    	width: 70%;
    }

    .close{
    	position: absolute;
    	right: 25px;
    	top: 0;
    	color: #000;
    	font-size: 35px;
    	font-weight: bold;
    }

    .close:hover,
    .close:focus{
    	color: red;
    	cursor: pointer;
    }

    .animate{
    	-webkit-animation: animatezoom 0.6s;
    	animation: animatezoom 0.6s;
    }

    @-webkit-keyframes animatezoom{
    	from{-webkit-transform: scale(0)}
    	to{-webkit-transform: scale(1)}
    	}
    </style>
    \n
    '''
