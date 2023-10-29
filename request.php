<?php

namespace App\Traits;
use GuzzleHttp\Client;

trait Request
{

    protected $client = null;

    protected function httpClient()
    {
        return  new Client(['base_uri' => $_ENV['API_URL']]);
    }

    /**
     *
     * @param mixed $url    base_uri defined already
     * @param mixed $method GET|POST|PUT|DELETE
     * 
     * @return Request
     */
    protected function httpGet($url, $method = 'GET') : Request
    {
        $client = new Client(['base_uri' => $_ENV['API_URL']]);
        $this->client =  $client->request($method, $url);
        return $this;
    }

    protected function httpPOST($url, $data = [], $method = 'POST')
    {
        $client = new Client();

        try {
            $response = $client->request('POST', $url);
    
            // Check if the response status code is 200 (OK)
            if ($response->getStatusCode() == 200) {
                // Parse the XML response
                $xmlResponse = $response->getBody();
                // You can now work with $xmlResponse, which contains the XML data
                return json_decode(json_encode(simplexml_load_file($xmlResponse)), true);
            } else {
                // Handle other status codes, if needed
                return "HTTP Request Failed: " . $response->getReasonPhrase();
            }
        } catch (\Exception $e) {
            // Handle exceptions, such as network errors
            return "HTTP Request Failed: " . $e->getMessage();
        }    
    }

    protected function body()
    {
        return json_decode($this->client->getBody()->getContents(), true);
    }

    /**
     * @param string|null $message message to flash
     * 
     * @return void
     */
    protected function back($type = null, $message = null)
    {
        if ($message) $_SESSION['flash'] = $message;
        if ($type) $_SESSION[$type] = $type;

        header('Location: ' . $_SERVER['HTTP_REFERER']);
        exit();
    }

    /**
     * @param string      $url     url to redirect back to
     * @param string|null $message message to flash
     * 
     * @return void
     */
    protected function redirect( string $url, $message = null )
    {
        if ($message) {
            $_SESSION['flash'] = $message;
        }
        header('Location: ' . $url);
        exit();
    }


    /**
     * @param string $key get post data
     * 
     * @return mixed
     */
    protected function param( string $key ) : mixed
    {
        return $_POST[ $key ] ?? null;
    }

    /**
     * @param mixed $type GET|POST|PUT|DELETE
     * 
     * @return bool
     */
    protected function method($type) : bool
    {
        return $_SERVER['REQUEST_METHOD'] == $type;
    }

    protected function getRequestPath()
    {
        return $_SERVER['REQUEST_URI'];
    }
}
