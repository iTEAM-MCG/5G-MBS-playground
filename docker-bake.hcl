variable "OPEN5GS_VERSION" {
  default = "v2.7.1"
}

variable "OPEN5GS_BRANCH" {
  default = "upv-mbs"
}

variable "UBUNTU_VERSION" {
  default = "jammy"
}

group "default" {
  targets = ["base-mbs-open5gs", "mb-smf", "mb-upf", "af"]
}

target "base-mbs-open5gs" {
  context = "./images/base-mbs-open5gs"
  tags = ["base-mbs-open5gs:${OPEN5GS_VERSION}"]
  output = ["type=image"]
}

target "mb-smf" {
  context = "./images/mb-smf"
  contexts = {
    "base-mbs-open5gs:${OPEN5GS_VERSION}" = "target:base-mbs-open5gs"
  }
  tags = ["mb-smf:${OPEN5GS_VERSION}"]
  output = ["type=image"]
}

target "mb-upf" {
  context = "./images/mb-upf"
  contexts = {
    "base-mbs-open5gs:${OPEN5GS_VERSION}" = "target:base-mbs-open5gs"
  }
  tags = ["mb-upf:${OPEN5GS_VERSION}"]
  output = ["type=image"]
}

target "af" {
  context = "."
  dockerfile = "./images/af/Dockerfile"
  tags = ["af:${OPEN5GS_VERSION}"]
  output = ["type=image"]
}
