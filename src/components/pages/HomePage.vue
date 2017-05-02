<template>
  <div class="main-page">
    <h2>AppointmentGuru DocumentGuru</h2>
    <!--<strong>Todo</strong>
    <ul>
      <li>Provide basic styling so that the App/docs looks nice</li>
    </ul>-->

    <h3>Upload an Image</h3>
     <div>
    <image-uploader ></image-uploader>
    </div>
    <!--<strong>Todo</strong>
    <ul>
      <li>Validate that images are the correct type, and (optionally) dimensions</li>
      <li>Upload images to the Actual API</li>
      <li>Show a loading icon while uploading</li>
    </ul>
    <strong>Example</strong>-->

    <hr/>

    <h3>Document list </h3>
    <p>Display a list of document items</p>
    <strong>Example</strong>
    <p>
    <document-list :documents='documents' ></document-list>
    </p>
    <hr/>


    <hr/>
  </div>
</template>

<script>
import ImageUploader from '@/components/ImageUploader'
import DocumentList from '@/components/DocumentList'

export default {
  name: 'homepage',
  components: {
    ImageUploader, DocumentList
  },
  data () {
    return {
      // todo: extra this into external files
      documents: [
        {
          id: 1,
          name: 'A name describing this file',
          type: 'application/pdf',
          url: 'http://someplace.com/foo'
        },
        {
          id: 2,
          name: 'A different name describing this file',
          type: 'application/pdf',
          url: 'http://someplace.com/foo'
        }
      ]
    }
  }
}
</script>
