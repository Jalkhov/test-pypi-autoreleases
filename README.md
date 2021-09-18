# test-pypi-autoreleases
Repo for test automation PyPI releases with Github Actions

[TestPyPi package](https://test.pypi.org/project/testing-pypi-autorelease/)

* Test 1 Failed due to workflow file error
* Test 2 Successfully
* Test 3 Create release but dont trigger upload_to_pypi workflow
* Test 4 Create release but dont trigger upload_to_pypi workflow, i will merge two workflows
* Test 5 Failed due to workflow file error
* Test 6 Successfully: Uploaded to PyPi and github release created
* Test 7 Successfully: But redirection in release notes to CHANGELOGS.md its a little ugly, i will try with multiline input in manual workflow
* Test 8 Failed: List element dont go to a new line and keep in header line, may force with a `<br>`?
