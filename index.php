<?php
/*
Copyright (C) 2014 TowerLabs

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the
Free Software Foundation, Inc., 51 Franklin Street,
Fifth Floor, Boston, MA  02110-1301, USA.
*/

$token = $_GET['token'];

$response = array();

header('Content-Type: application/json');

error_reporting(0);
ini_set("log_errors", 1);
ini_set("error_log", "./logs/error.log");

if(isset($token) && !empty($token) && 'token' == $token)
{
    try
    {
        $dir      = '.';
        $files    = glob('./*.flist', GLOB_BRACE);
        sort($files);
        $filename = array_pop($files);

        $handle   = fopen($filename, "r");	
        $contents = fread($handle, filesize($filename));

        fclose($handle);
        echo json_encode(json_decode($contents),JSON_PRETTY_PRINT);
	}
    catch(Exception $e)
    {
        error_log( $e->getMessage() );
    }
}
else
{
    $response['err'] = 1;
    $response['msg'] = 'Token is required';
    echo json_encode($response,JSON_PRETTY_PRINT);
}
exit;
?>